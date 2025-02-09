"use client";

import { cn } from "@/lib/style";
import { useRouter } from "next/navigation";
import { useActionState, useEffect } from "react";
import { useToast } from "@/hooks/use-toast";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import {
	Select,
	SelectContent,
	SelectItem,
	SelectTrigger,
	SelectValue,
} from "@/components/ui/select";
import {
	Card,
	CardHeader,
	CardTitle,
	CardDescription,
	CardContent,
} from "@/components/ui/card";
import { createAction } from "@/server-actions/chatbot-index/create";

type Props = {
	chatbotId: string
	className?: string;
};

export const CreateChatbotIndexForm = ({ chatbotId, className }: Props) => {
	const router = useRouter();
	const { toast } = useToast();

	const [state, formAction, isPending] = useActionState(createAction, {
		inputs: {
			chatbotId: chatbotId,
			meta: {
				resource: "openai"
			},
			title: "",
			content: ""
		},
	});

	useEffect(() => {
		if (state.success) {
			toast({
				title: "Success",
				description: "Create Chatbot Successfully",
			});
			router.push("/chatbot");
		} else if (state.success === false) {
			toast({
				variant: "destructive",
				title: "Error",
				description: "Error while Creating Chatbot",
			});
		}
	}, [state]);

	return (
		<form
			action={formAction}
			className={cn(
				`w-full flex flex-col justify-center items-center`,
				className,
			)}
		>
			<Card className={`w-full`}>
				<CardHeader>
					<CardTitle>Create Index</CardTitle>
					<CardDescription>Chat with LLM</CardDescription>
				</CardHeader>
				<CardContent className="flex flex-col gap-3">
					<div className={"flex gap-1.5"}>
						<Label className={'flex flex-col gap-1.5'}>
							LLM
							<Select
								key={state.inputs?.meta.resource}
								name={"inputs.meta.resource"}
								defaultValue={state.inputs?.meta.resource}
							>
								<SelectTrigger className="w-[120px]">
									<SelectValue />
								</SelectTrigger>
								<SelectContent>
									<SelectItem value="openai">OpenAI</SelectItem>
									<SelectItem value="google">Google</SelectItem>
									<SelectItem value="anthropic">Anthropic</SelectItem>
								</SelectContent>
							</Select>
						</Label>
					</div>
					<Input
						type={"hidden"}
						key={state.inputs?.chatbotId}
						name={"inputs.chatbotId"}
						defaultValue={state.inputs?.chatbotId}
					/>
					<Label className={'flex flex-col gap-1.5'}>
						Title
						<Input
							type={"text"}
							name={"inputs.title"}
							defaultValue={state.inputs?.title}
							className={state.validationErrors?.title && "bg-red-200"}
						/>
						{state.validationErrors?.title && (
							<small>{state.validationErrors?.title}</small>
						)}
					</Label>
					<Label className={'flex flex-col gap-1.5'}>
						コンテンツ
						<Textarea
							className={"resize-none h-full"}
							key={state.inputs?.content}
							name={"inputs.content"}
							defaultValue={state.inputs?.content}
							placeholder={""}
						/>
						{state.validationErrors?.content && (
							<small>{state.validationErrors?.content}</small>
						)}
					</Label>
					<Button type="submit" disabled={isPending}>
						Create Index
					</Button>
				</CardContent>
			</Card>
		</form>
	);
};
